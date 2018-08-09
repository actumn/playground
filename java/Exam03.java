import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;

public class Exam03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[][] input = {
				{0, 1, 0, 1, 0, 1, 0, 1},
				{0, 0, 0, 0, 0, 1, 0, 0},
				{1, 0, 1, 0, 0, 1, 0, 1},
				{0, 0, 0, 0, 0, 0, 0, 0},
				{0, 0, 0, 1, 0, 0, 0, 0},
				{0, 0, 0, 0, 0, 1, 0, 1},
				{0, 1, 0, 0, 0, 0, 0, 0},
				{0, 0, 0, 0, 1, 0, 1, 0}
		};

		solution(input);//.print();
	}

	private static Result solution(int[][] input) {
		int horlen = input[0].length; int verlen = input.length;

		int[][] horCons = new int[horlen][verlen];
		int[][] verCons = new int[horlen][verlen];
		for (int i = 0; i < verlen; i++) {
			Arrays.fill(horCons[i], -1);
			Arrays.fill(verCons[i], -1);
		}


		int index = 0;
		for (int i = 0; i < verlen; i++) {
			for (int j = 0; j < horlen; j++) {
				if (input[i][j] == 1) {
					if (j != 0 && j != horlen-1 && input[i][j-1] != 1)
						index++;
					continue;
				}

				horCons[i][j] = index;
			}
			index++;
		}
		index = 0;
		for (int j = 0; j < horlen; j++) {
			for (int i = 0; i < verlen; i++) {
				if (input[i][j] == 1) {
					if (i != 0 && i != verlen-1 && input[i-1][j] != 1)
						index++;
					continue;
				}

				verCons[i][j] = index;
			}
			index++;
		}

		List<Pair<Integer, Integer>> consList = new LinkedList<>();
		for (int i = 0; i < verlen; i++) {
			for (int j = 0; j < horlen; j++) {
				if (input[i][j] == 1) continue;
				consList.add(new Pair(horCons[i][j], verCons[i][j]));
			}
		}

		return recursiveCalculation(consList, new Result());
	}

	private static Result recursiveCalculation(List<Pair<Integer, Integer>> consList, Result result) {
		List<Pair<Integer, Integer>> subList = new LinkedList<>();
		result.addCur();

		result.subCur();
		return result;
	}
}

class Result {
	int max;
	int combinations;
	int currNumber;

	Result() {
		this.max = 0;
		this.combinations = 0;
		this.currNumber = 0;
	}

	void addCur() {
		this.currNumber += 1;
	}
	void subCur() {
		this.currNumber -= 1;
	}

	void print() {
		System.out.println("최대 "+max+"명, "+combinations+"가지");
	}
}

class Pair<L, R> {
	final L left;
	final R right;

	public Pair(L left, R right) {
		this.left = left;
		this.right = right;
	}

	public L getLeft() { return left; }
	public R getRight() { return right; }

	@Override
	public int hashCode() { return left.hashCode() ^ right.hashCode(); }

	@Override
	public boolean equals(Object o) {
		if (!(o instanceof Pair)) return false;
		Pair pairo = (Pair) o;
		return this.left.equals(pairo.getLeft()) &&
				this.right.equals(pairo.getRight());
	}
}
