package kotlinloader

class KotlinTest {

    /**
     * Always returns true. Just here to help test that Kotlin actually loaded, and works correctly.
     */
    fun test(): Boolean {
        return true;
    }

    /**
     * Returns the current Kotlin version. It's safe to assume if this function returns an NullPointerException that the current version is 0.12.613.
     */
    fun getKotlinVersion(): String {
        return "0.12.613"
    }

}