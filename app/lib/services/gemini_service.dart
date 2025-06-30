// lib/services/gemini_service.dart
import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

class GeminiService {
  late final WebSocketChannel _channel;

  GeminiService() {
    _channel = WebSocketChannel.connect(Uri.parse('ws://YOUR_BACKEND_URL/ws'));
  }

  void sendText(String text) {
    _channel.sink.add(jsonEncode({'text': text}));
  }

  void sendAudio(List<int> audioBytes) {
    final base64Audio = base64Encode(audioBytes);
    _channel.sink.add(
      jsonEncode({
        'audio': {
          'mime_type': 'audio/webm', // or your audio format
          'data': base64Audio,
        },
      }),
    );
  }

  Stream<dynamic> get responses => _channel.stream;

  void dispose() {
    _channel.sink.close();
  }
}
