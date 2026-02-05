import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Text } from '@/components/ui/text';
import { confirmSignUp, resendSignUpCode } from 'aws-amplify/auth';
import { router, useLocalSearchParams } from 'expo-router';
import { AlertCircleIcon, CheckCircle2Icon } from 'lucide-react-native';
import * as React from 'react';
import { View } from 'react-native';

export default function VerifyEmailScreen() {
  const { email } = useLocalSearchParams<{ email: string }>();
  const [code, setCode] = React.useState('');
  const [error, setError] = React.useState('');
  const [isLoading, setIsLoading] = React.useState(false);
  const [isResending, setIsResending] = React.useState(false);
  const [resendSuccess, setResendSuccess] = React.useState(false);

  async function onSubmit() {
    setError('');

    if (!code.trim()) {
      setError('Please enter the verification code');
      return;
    }

    if (!email) {
      setError('Email address is missing. Please sign up again.');
      return;
    }

    setIsLoading(true);

    try {
      const { isSignUpComplete, nextStep } = await confirmSignUp({
        username: email,
        confirmationCode: code,
      });

      console.log('Verification result:', { isSignUpComplete, nextStep });

      // Navigate to sign-in page after successful verification
      router.replace('/auth');
    } catch (err: any) {
      console.error('Verification error:', err);

      // Handle specific Cognito errors
      if (err.name === 'CodeMismatchException') {
        setError('Invalid verification code. Please check and try again.');
      } else if (err.name === 'ExpiredCodeException') {
        setError('Verification code has expired. Please request a new code.');
      } else if (err.name === 'LimitExceededException') {
        setError('Too many attempts. Please try again later.');
      } else {
        setError(err.message || 'Failed to verify code. Please try again.');
      }
    } finally {
      setIsLoading(false);
    }
  }

  async function handleResendCode() {
    setError('');
    setResendSuccess(false);

    if (!email) {
      setError('Email address is missing. Please sign up again.');
      return;
    }

    setIsResending(true);

    try {
      await resendSignUpCode({ username: email });
      setResendSuccess(true);
      setTimeout(() => setResendSuccess(false), 5000); // Hide success message after 5 seconds
    } catch (err: any) {
      console.error('Resend code error:', err);
      setError(err.message || 'Failed to resend code. Please try again.');
    } finally {
      setIsResending(false);
    }
  }

  return (
    <View className="flex-1 items-center justify-center p-4">
      <View className="w-full max-w-sm">
        <View className="gap-6">
          <Card className="border-border/0 sm:border-border shadow-none sm:shadow-sm sm:shadow-black/5">
            <CardHeader>
              <CardTitle className="text-center text-xl sm:text-left">
                Verify your email
              </CardTitle>
              <CardDescription className="text-center sm:text-left">
                We sent a verification code to {email}
              </CardDescription>
            </CardHeader>
            <CardContent className="gap-6">
              <View className="gap-6">
                {error ? (
                  <Alert icon={AlertCircleIcon} variant="destructive">
                    <AlertTitle>Error</AlertTitle>
                    <AlertDescription>{error}</AlertDescription>
                  </Alert>
                ) : null}
                {resendSuccess ? (
                  <Alert icon={CheckCircle2Icon}>
                    <AlertTitle>Code sent</AlertTitle>
                    <AlertDescription>
                      A new verification code has been sent to your email.
                    </AlertDescription>
                  </Alert>
                ) : null}
                <View className="gap-1.5">
                  <Label htmlFor="code">Verification Code</Label>
                  <Input
                    id="code"
                    placeholder="123456"
                    keyboardType="number-pad"
                    autoComplete="one-time-code"
                    value={code}
                    onChangeText={setCode}
                    returnKeyType="send"
                    onSubmitEditing={onSubmit}
                    editable={!isLoading}
                    maxLength={6}
                  />
                </View>
                <Button className="w-full" onPress={onSubmit} disabled={isLoading}>
                  <Text>{isLoading ? 'Verifying...' : 'Verify Email'}</Text>
                </Button>
              </View>
              <View className="flex-row items-center justify-center gap-1">
                <Text className="text-center text-sm">Didn&apos;t receive the code?</Text>
                <Button
                  variant="link"
                  size="sm"
                  className="web:h-fit h-4 px-0 py-0 sm:h-4"
                  onPress={handleResendCode}
                  disabled={isResending || isLoading}>
                  <Text className="text-sm font-normal">
                    {isResending ? 'Sending...' : 'Resend'}
                  </Text>
                </Button>
              </View>
            </CardContent>
          </Card>
        </View>
      </View>
    </View>
  );
}
