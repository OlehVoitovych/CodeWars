import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.assertThat;

public class Tests {
    @Test
    public void testExampleFromDescription() {
        assertThat(CustomeMorseCode.decode(".... . -.--   .--- ..- -.. ."), is("HEY JUDE"));
    }
}
