Kotlin Loader
====

Kotlin loader. Contains Kotlin runtime class files so that any Bukkit plugin that uses Kotin loads successfully.

Getting a Jar
----

To get a jar with the Kotlin runtime, run the following commands in the repository root:

```
$ unzip kotlin-runtime.zip
$ gradle build shadowJar
```

The finished jar is in build/libs with a name similar to `Kotlin-Loader-all.jar`.

Usage
----

In your `plugin.yml`, place the following:

```
depends: [KotlinLoader]
```

Standard Disclaimer
====

I am not claiming I'm a developer of Kotlin, or anything similar. I am just making a loader so that Bukkit plugins can
work if they're made in Kotlin.