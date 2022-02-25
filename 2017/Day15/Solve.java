import java.util.ArrayList;

class Solve {
    public static void main(String[] args) {
        long genA = 783;
        long genB = 325;
        final int aFactor = 16807;
        final int bFactor = 48271;
        final int mod = 2147483647;

        ArrayList<Long> aList = new ArrayList<Long>(5000000);
        ArrayList<Long> bList = new ArrayList<Long>(5000000);

        int count1 = 0;
        int count2 = 0;

        for (int i = 0; i < 40000000; i++){
            genA = (genA * aFactor) % mod;
            genB = (genB * bFactor) % mod;

            if ((genA & 0xFFFF) == (genB & 0xFFFF)){
                count1 = count1 + 1;
            }

            if (Math.min(aList.size(), bList.size()) > 5000000){
                continue;
            }

            if (genA % 4 == 0){
                aList.add(genA);
            }

            if (genB % 8 == 0){
                bList.add(genB);
            }
        }

        for (int i = 0; i < 5000000; i++){
            if ((aList.get(i) & 0xFFFF) == (bList.get(i) & 0xFFFF)){
                count2 = count2 + 1;
            }
        }
        System.out.println(count1);
        System.out.println(count2);
    }
}