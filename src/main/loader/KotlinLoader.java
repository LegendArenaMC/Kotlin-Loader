import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

/**
 * Created on 6/26/2015
 *
 * @author ThePixelDev
 */
public class KotlinLoader extends JavaPlugin {

    public void onEnable() {
        try {
            new KotlinText().test();
        } catch(Exception ex) {
            Bukkit.getLogger().severe("Error! Kotlin Loader couldn't test Kotlin successfully. (is the Kotlin runtime in the jar?)");
            setEnabled(false);
            return;
        }
        Bukkit.getLogger().info("Kotlin loader enabled! Enjoy your Kotlin-based plugins.");
    }

    public void onDisable() {}

}
