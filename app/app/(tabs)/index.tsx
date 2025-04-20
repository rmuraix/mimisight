import { CameraView, useCameraPermissions } from "expo-camera";
import { Button, StyleSheet, Text, View } from "react-native";

export default function App() {
  const [permission, requestPermission] = useCameraPermissions();

  if (!permission) {
    // カメラパーミッションがロード中
    return <View />;
  }

  if (!permission.granted) {
    // カメラ許可がまだない場合に許可のためのUI要素などを出す
    return (
      <View style={styles.container}>
        <Text style={styles.message}>
          We need your permission to show the camera
        </Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <CameraView style={styles.camera} facing="back" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
  },
  message: {
    textAlign: "center",
    paddingBottom: 10,
  },
  camera: {
    flex: 1,
  },
  button: {
    flex: 1,
    alignSelf: "flex-end",
    alignItems: "center",
  },
  text: {
    fontSize: 24,
    fontWeight: "bold",
    color: "white",
  },
});
