// lib/components/themed_text.dart
import 'package:flutter/material.dart';

class ThemedText extends StatelessWidget {
  final String text;
  final String type;

  const ThemedText(this.text, {super.key, this.type = 'default'});

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme;
    TextStyle? style;
    switch (type) {
      case 'title':
        style = textTheme.headlineLarge;
        break;
      case 'subtitle':
        style = textTheme.titleMedium;
        break;
      // ... 他のスタイルを定義
      default:
        style = textTheme.bodyMedium;
    }
    return Text(text, style: style);
  }
}
