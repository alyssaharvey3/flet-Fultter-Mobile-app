import 'package:flutter/widgets.dart';
import '../models/control.dart';
import 'create_control.dart';

class StackControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final bool parentDisabled;
  final List<Control> children;

  const StackControl(
      {Key? key,
      this.parent,
      required this.control,
      required this.children,
      required this.parentDisabled})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    debugPrint("Stack build: ${control.id}");

    bool disabled = control.attrBool("disabled", false)! || parentDisabled;

    return expandable(
        Stack(
          children: control.childIds
              .map((childId) => createControl(control, childId, disabled))
              .toList(),
        ),
        control);
  }
}
