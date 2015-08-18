import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;
import kotlinloader.KotlinTest;

public class KotlinLoader extends JavaPlugin {

    public void onEnable() {
        try {
            new KotlinTest().test();
        } catch(Exception ex) {
            getLogger().severe("Error! Kotlin Loader couldn't test Kotlin successfully. (is the Kotlin runtime in the shadowed jar?)");
            setEnabled(false);
            return;
        }
    }

    public void onDisable() {}

}
