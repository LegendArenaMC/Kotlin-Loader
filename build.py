#!/usr/bin/python3
import os

cd = os.system("cd kotlinc &> /dev/null && cd ..")

if cd is not 0:
    os.system("wget https://github.com/JetBrains/kotlin/releases/download/build-0.12.613/kotlin-compiler-0.12.613.zip")
    os.system("unzip kotlin-compiler-0.12.613.zip &>/dev/null")
    os.system("rm *.zip &>/dev/null")

gradle = os.system("gradle --help &>/dev/null")
if gradle is not 0:
    os.system("gradle build shadowJar")
else:
    os.system("chmod +x ./gradlew")
    os.system("./gradlew build --no-daemon && rm build/libs/*.jar")
os.system("cp src/main/java/KotlinTest.kt . &>/dev/null")
os.system("./kotlinc/bin/kotlinc-jvm KotlinTest.kt -include-runtime -d KotlinLoader.jar")
os.system("rm ./*.kt &> /dev/null")
os.system("mv ./*.jar build/libs &> /dev/null")
#os.system("mkdir SHADEME")
#os.system("cp build/classes/main/KotlinLoader.class SHADEME")
#os.system("cp src/main/resources/plugin.yml SHADEME")
os.system("mv build/libs/*-all.jar ./KotlinLoader.jar")