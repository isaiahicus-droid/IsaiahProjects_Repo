# McModingStart

A minimal Fabric mod project for Minecraft 26.3.

## Requirements

- Java 25
- Internet access for Gradle to download the build dependencies

## Build

From the repository root, run:

```sh
./Java/gradlew -p Java build
```

Or, from this `Java` directory, run:

```sh
./gradlew build
```

The mod initializer is `src/main/java/com/isaiahicus/mcmodingstart/McModingStart.java`.
Add common initialization code in its `onInitialize` method. This project uses
Loom's default Mojang mappings; Yarn mappings are not published for Minecraft
26.3.

## Verified toolchain

- Minecraft 26.3
- Fabric Loader 0.19.5
- Fabric API 0.162.0+26.3
- Fabric Loom 1.18.3
- Gradle wrapper 9.7.1
