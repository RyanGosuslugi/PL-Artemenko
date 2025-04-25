import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Введите число: ");
        int number = scanner.nextInt();
        
        System.out.print("Введите начальную степень: ");
        int startPower = scanner.nextInt();
        
        boolean found = false;
        int[] multipliers = {1, 2, 4, 8, 16, 32, 64};
        
        // Вычисляем сумму степеней цифр
        int sum = calculatePowerSum(number, startPower);
        
        // Проверяем, равна ли сумма числу умноженному на один из множителей
        for (int multiplier : multipliers) {
            if (sum == number * multiplier) {
                System.out.printf("sC(%d, %d) => сумма = %d = %d * %d%n", 
                                 number, startPower, sum, number, multiplier);
                found = true;
                break;
            }
        }
        
        if (!found) {
            System.out.printf("sC(%d, %d) => сумма = %d, не соответствует условию%n", 
                             number, startPower, sum);
        }
    }
    
    // Метод для вычисления суммы степеней цифр числа
    private static int calculatePowerSum(int number, int startPower) {
        String numStr = Integer.toString(number);
        int sum = 0;
        int currentPower = startPower;
        
        for (int i = 0; i < numStr.length(); i++) {
            int digit = Character.getNumericValue(numStr.charAt(i));
            sum += Math.pow(digit, currentPower);
            currentPower++;
        }
        
        return sum;
    }
}