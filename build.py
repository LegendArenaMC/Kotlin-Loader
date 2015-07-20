#!/usr/bin/python3
import os
#wget https://github.com/JetBrains/kotlin/releases/download/build-0.12.613/kotlin-compiler-0.12.613.zip
#unzip kotlin-compiler-0.12.613.zip
#rm *.zip
#gradle build
#cp src/main/java/KotlinTest.kt .
#./kotlinc/bin/kotlinc-jvm KotlinTest.kt -include-runtime -d KotlinLoader.jar

cd = os.system("cd kotlinc &> /dev/null && cd ..")

if cd is not 0:
    os.system("wget https://github.com/JetBrains/kotlin/releases/download/build-0.12.613/kotlin-compiler-0.12.613.zip")
    os.system("unzip kotlin-compiler-0.12.613.zip")
    os.system("rm *.zip &> /dev/null")

os.system("chmod +x ./gradlew")
os.system("./gradlew build --no-daemon && rm build/libs/*.jar")
os.system("cp src/main/java/KotlinTest.kt . &>/dev/null")
os.system("./kotlinc/bin/kotlinc-jvm KotlinTest.kt -include-runtime -d KotlinLoader.jar")
os.system("rm ./*.kt &> /dev/null")
os.system("mv ./*.jar build/libs &> /dev/null")
os.system("mkdir SHADEME")
os.system("cp build/classes/main/KotlinLoader.class SHADEME")
os.system("cp src/main/resources/plugin.yml SHADEME")
print(" ")
print("You may want to move the files in the \"SHADEME\" folder into the jar so the plugin functions.")
print("(sorry, too lazy to care about finding out how the fuck to do this via Bash/Zsh/whatever the fuck shell you use)")
print(" ")