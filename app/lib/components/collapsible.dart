// lib/components/collapsible.dart
import 'package:flutter/material.dart';

class Collapsible extends StatelessWidget {
  final String title;
  final Widget child;

  const Collapsible({super.key, required this.title, required this.child});

  @override
  Widget build(BuildContext context) {
    return ExpansionTile(
      title: Text(title),
      children: [
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16.0),
          child: child,
        ),
      ],
    );
  }
}
