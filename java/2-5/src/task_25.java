
public class task_25 {
	
	//2.1 ���������� ����� ��������
	public static int GCD(int a, int b) { return b==0 ? a : GCD(b, a%b); }
	
	//2.2 ����� ���� �����
	public static int SumN(int n){
		int sum = 0;
		while(n != 0){
		        sum += (n % 10);
		        n/=10;
		}
		return sum;
	}
}