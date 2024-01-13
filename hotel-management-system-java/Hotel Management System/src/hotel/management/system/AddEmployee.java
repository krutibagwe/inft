package hotel.management.system;


import java.awt.EventQueue;


import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class AddEmployee extends JFrame{ //Third Frame

    
	JTextField textField,textField_1,textField_2,textField_3,textField_4,textField_5,textField_6;
        JComboBox c1;

        public AddEmployee(){
            getContentPane().setForeground(Color.BLUE);
            getContentPane().setBackground(Color.WHITE);
            setTitle("ADD EMPLOYEE DETAILS");
		 
            setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
            setSize(1200,600);
            setLocation(50,50);
            getContentPane().setLayout(null);
			
            JLabel Passportno = new JLabel("NAME");
            Passportno.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Passportno.setBounds(60, 70, 150, 27);
            add(Passportno);
            
            textField = new JTextField();
            textField.setBounds(200, 70, 150, 27);
            add(textField);
			
            JButton Next = new JButton("SAVE");
            Next.setBounds(220, 480, 130, 30);
            Next.setBackground(Color.BLACK);
            Next.setForeground(Color.WHITE);
            add(Next);
            
           
            
            JButton btnExit = new JButton("Back");
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
                                setVisible(false);
			}
		});
		btnExit.setBounds(50, 480, 130, 30);
                btnExit.setBackground(Color.BLACK);
                btnExit.setForeground(Color.WHITE);
		add(btnExit);
            
           
			
            JLabel Pnrno = new JLabel("AGE");
            Pnrno.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Pnrno.setBounds(60, 120, 150, 27);
            add(Pnrno);
			
            textField_1 = new JTextField();
            textField_1.setBounds(200, 120, 150, 27);
            add(textField_1);
            
            
            JLabel Gender = new JLabel("GENDER");
            Gender.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Gender.setBounds(60, 170, 150, 27);
            add(Gender);
		
            JRadioButton NewRadioButton = new JRadioButton("MALE");
            NewRadioButton.setBackground(Color.WHITE);
            NewRadioButton.setBounds(200, 170, 70, 27);
            add(NewRadioButton);
	
            JRadioButton Female = new JRadioButton("FEMALE");
            Female.setBackground(Color.WHITE);
            Female.setBounds(280, 170, 70, 27);
            add(Female);
            
            
            JLabel Address = new JLabel("JOB");
            Address.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Address.setBounds(60, 220, 150, 27);
            add(Address);
			
            String course[] = {"Front Desk Clerks","Housekeeping","Kitchen Staff","Room Service","Waiter","Manager","Chef"};
            c1 = new JComboBox(course);
            c1.setBackground(Color.WHITE);
            c1.setBounds(200,220,150,30);
            add(c1);
            		
            JLabel Nationality = new JLabel("SALARY");
            Nationality.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Nationality.setBounds(60, 270, 150, 27);
            add(Nationality);
			
            textField_3 = new JTextField();
            textField_3.setBounds(200, 270, 150, 27);
            add(textField_3);
	
            JLabel Name = new JLabel("PHONE");
            Name.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Name.setBounds(60, 320, 150, 27);
            add(Name);
	
            textField_4 = new JTextField();
            textField_4.setBounds(200, 320, 150, 27);
            add(textField_4);
	
            JLabel Phno = new JLabel("AADHAR");
            Phno.setFont(new Font("Tahoma", Font.PLAIN, 17));
            Phno.setBounds(60, 370, 150, 27);
            add(Phno);
			
            textField_5 = new JTextField();
            textField_5.setBounds(200, 370, 150, 27);
            add(textField_5);
	
            
            JLabel email = new JLabel("EMAIL");
            email.setFont(new Font("Tahoma", Font.PLAIN, 17));
            email.setBounds(60, 420, 150, 27);
            add(email);
			
            textField_6 = new JTextField();
            textField_6.setBounds(200, 420, 150, 27);
            add(textField_6);
	
            setVisible(true);
	
           
            
             JLabel l10 = new JLabel("Add Employee Details");
            l10.setFont(new Font("Tahoma", Font.BOLD, 25));
            l10.setBounds(194, 10, 300, 30);
            add(l10);
			    
      
            
             ImageIcon i1  = new ImageIcon(ClassLoader.getSystemResource("images/hotel51.jpg"));
                Image i3 = i1.getImage().getScaledInstance(600, 350,Image.SCALE_DEFAULT);
                ImageIcon i2 = new ImageIcon(i3);
                JLabel l15 = new JLabel(i2);
                l15.setBounds(500,90,600,350);
                add(l15);

            
            Next.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent ae) {
        Conn c = new Conn();
        String gender = null;

        if (NewRadioButton.isSelected()) {
            gender = "male";
        } else if (Female.isSelected()) {
            gender = "female";
        }

        String s6 = (String) c1.getSelectedItem();

        try {
            String name = textField.getText();
            String age = textField_1.getText();
            String salary = textField_3.getText();
            String phone = textField_4.getText();
            String aadhar = textField_5.getText();
            String email = textField_6.getText();

            
            
            if (name.isEmpty() || age.isEmpty() || salary.isEmpty() || phone.isEmpty() || aadhar.isEmpty() || email.isEmpty()) {
                JOptionPane.showMessageDialog(null, "Please fill all the details.");
                return; 
            }

            if (!name.matches("^[a-zA-Z]*$")) {
                JOptionPane.showMessageDialog(null, "Name should contain only characters (A-Z or a-z)");
                return; 
            }

            String emailRegex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
            Pattern pattern = Pattern.compile(emailRegex);
            Matcher matcher = pattern.matcher(email);

            if (!matcher.matches()) {
                JOptionPane.showMessageDialog(null, "Invalid Email Address");
                return; 
            }

            if (!phone.matches("^\\d{10}$")) {
                JOptionPane.showMessageDialog(null, "Phone number should contain exactly 10 digits");
                return; 
            }

            String str = "INSERT INTO employee values( '" + name + "', '" + age + "', '" + gender + "','" + s6 + "', '" + salary + "', '" + phone + "','" + aadhar + "', '" + email + "')";

            c.s.executeUpdate(str);
            JOptionPane.showMessageDialog(null, "Employee Added");
            setVisible(false);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
});

			
            setSize(1200,600);
            setVisible(true);
            setLocation(150,100);
			
	}
        
        
    public static void main(String[] args){
        new AddEmployee();
    }   
}


