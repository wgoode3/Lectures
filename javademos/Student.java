public class Student extends Person {
	private String location;
	public Student(String name, int age, String location){
		super(name, age);
		this.location = location;
	}

	public void status(){
		System.out.println(this.name + " is a student at " + this.location + ".");
	}
}