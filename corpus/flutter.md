


Flutter is Google's mobile app SDK for crafting high-quality native interfaces
on iOS and Android in record time. Flutter works with existing code, is used by
developers and organizations around the world, and is free and open source.
Documentation

Install Flutter
Flutter documentation
Development wiki
Contributing to Flutter

For announcements about new releases and breaking changes, follow the
flutter-announce@googlegroups.com
mailing list.
About Flutter
We think Flutter will help you create beautiful, fast apps, with a productive,
extensible and open development model.
Beautiful apps
We want to enable designers to deliver their full creative vision without being
forced to water it down due to limitations of the underlying framework.
Flutter's layered architecture gives you control over every pixel on the
screen, and its powerful compositing capabilities let you overlay and animate
graphics, video, text and controls without limitation. Flutter includes a full
set of widgets that deliver pixel-perfect experiences on both
iOS and Android.

Fast apps
Flutter is fast. It's powered by the same hardware-accelerated Skia 2D
graphics library that underpins Chrome and Android. We architected Flutter to
support glitch-free, jank-free graphics at the native speed of your device.
Flutter code is powered by the world-class Dart platform, which enables
compilation to native 32-bit and 64-bit ARM code for iOS and Android.
Productive development
Flutter offers stateful hot reload, allowing you to make changes to your code
and see the results instantly without restarting your app or losing its state.

Extensible and open model
Flutter works with any development tool, but includes editor plug-ins for both
Visual Studio Code and IntelliJ / Android Studio. Flutter provides
thousands of packages to speed your development, regardless
of your target platform. And accessing platform features is easy. Here is a
snippet from our interop example:
Future<void> getBatteryLevel() async {
  var batteryLevel = 'unknown';
  try {
    int result = await methodChannel.invokeMethod('getBatteryLevel');
    batteryLevel = 'Battery level: $result%';
  } on PlatformException {
    batteryLevel = 'Failed to get battery level.';
  }
  setState(() {
    _batteryLevel = batteryLevel;
  });
}
Flutter is a fully open source project, and we welcome contributions.
Information on how to get started can be found at our
contributor guide.
