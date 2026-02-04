import { SignUpForm } from '@/components/sign-up-form';
import { View } from 'react-native';

export default function SignUpScreen() {
  return (
    <View className="flex-1 items-center justify-center p-4">
      <View className="w-full max-w-sm">
        <SignUpForm />
      </View>
    </View>
  );
}
