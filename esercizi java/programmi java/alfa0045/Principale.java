package alfa0045;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class Principale {
    public static void main(String[] args) {
        Map<String,String> map = new HashMap<String,String>();
        map.put("1","jan");
        map.put("2","feb");
        map.put("3","mar");
        map.put("4","apr");
        map.put("5","may");
        map.put("6","jun");

        Iterator<Entry<String,String>> iterator = map.entrySet().iterator();
        while (iterator.hasNext()){
            Map.Entry<String,String> entry = (Map.Entry<String,String>) iterator.next();
            System.out.println("key: "+entry.getKey()+" value: "+entry.getValue());
        }
    }
}
