import java.io.File;
import java.io.IOException;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class ApkAnalyzer {

    public static void main(String[] args) {
        String apkFilePath = "path/to/apk/file.apk";
        try {
            ZipFile apkFile = new ZipFile(new File(apkFilePath));
            Enumeration<? extends ZipEntry> entries = apkFile.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();
                System.out.println(entry.getName());
            }
            apkFile.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
