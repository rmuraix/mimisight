import { Link } from "expo-router";
import { StyleSheet, TouchableOpacity } from "react-native";

import { ThemedText } from "@/components/ThemedText";
import { ThemedView as View } from "@/components/ThemedView";
import { Colors } from "@/constants/Colors";

export default function TabOneScreen() {
  return (
    <View style={styles.container}>
      <ThemedText style={styles.title}>MimiSight</ThemedText>

      <View
        style={styles.separator}
        lightColor="#eee"
        darkColor="rgba(255,255,255,0.1)"
      />

      <Link href="/camera" asChild>
        <TouchableOpacity style={styles.cameraButton}>
          <ThemedText style={styles.cameraButtonText}>
            カメラで認識を開始
          </ThemedText>
        </TouchableOpacity>
      </Link>

      <View style={styles.infoContainer}>
        <ThemedText style={styles.infoText}>
          このアプリはカメラで捉えた映像を認識し、視覚情報を音声で説明します。
          {"\n\n"}
          現在はデモ版です。後ほどサーバーと連携して実際の認識機能が追加される予定です。
        </ThemedText>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: "bold",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  cameraButton: {
    backgroundColor: Colors.light.tint,
    paddingHorizontal: 20,
    paddingVertical: 15,
    borderRadius: 10,
    marginVertical: 20,
  },
  cameraButtonText: {
    color: "white",
    fontSize: 18,
    fontWeight: "bold",
  },
  infoContainer: {
    marginTop: 20,
    paddingHorizontal: 20,
  },
  infoText: {
    textAlign: "center",
    lineHeight: 24,
  },
});
