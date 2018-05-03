public class Wizard extends Person {
	private int mana;
	private static int count = 0;

	public Wizard(String name, int age, String personality, int mana){
		super(name, age, personality);
		this.mana = mana;
		count++;
	} 

	public void explosion(){
		if( this.mana >= 50 ){
			System.out.println(this.name + " casts a powerful explosion spell");
			this.mana -= 50;
		}else{
			System.out.println(this.name + " is out of mana.");
		}
	}

	public void numberOfWizards(){
		System.out.println(count);
	}
}