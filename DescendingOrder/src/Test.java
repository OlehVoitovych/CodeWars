import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class Test {
    @org.junit.Test
    public void test_01() {
        assertEquals(0, DescendingOrder.sortDesc(0));
    }

    @org.junit.Test
    public void test_02() {
        assertEquals(51, DescendingOrder.sortDesc(15));
    }


    @org.junit.Test
    public void test_03() {
        assertEquals(987654321, DescendingOrder.sortDesc(123456789));
    }
}
