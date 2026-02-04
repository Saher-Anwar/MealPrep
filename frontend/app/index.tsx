import { SignInForm } from '@/components/sign-in-form';
import { Stack } from 'expo-router';
import { View } from 'react-native';

const SCREEN_OPTIONS = {
  title: 'Sign In',
  headerShown: false,
};

export default function SignInScreen() {
  return (
    <>
      <Stack.Screen options={SCREEN_OPTIONS} />
      <View className="flex-1 items-center justify-center p-4">
        <View className="w-full max-w-sm">
          <SignInForm />
        </View>
      </View>
    </>
  );
}
