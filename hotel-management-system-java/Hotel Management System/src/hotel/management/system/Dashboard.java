package hotel.management.system;


import java.awt.*;
import javax.swing.*;
import java.awt.event.*;


public class Dashboard extends JFrame{

    public static void main(String[] args) {
        new Dashboard().setVisible(true);
    }
    
    public Dashboard() {
        super("StayInnSight");
	
        setForeground(Color.CYAN);
        setLayout(null); 

        
        ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("images/hotel4.jpg"));
        Image i2 = i1.getImage().getScaledInstance(1200, 600,Image.SCALE_DEFAULT);
        ImageIcon i3 = new ImageIcon(i2); 
	JLabel NewLabel = new JLabel(i3);
	NewLabel.setBounds(0, 0, 1200, 600); 
        add(NewLabel);
        	
        JMenuBar menuBar = new JMenuBar();
	setJMenuBar(menuBar);
		
        JMenu HotelSystem = new JMenu("MANAGE HOTEL");
        HotelSystem.setForeground(Color.BLUE);
	menuBar.add(HotelSystem);
        
        
		
        JMenuItem Recep = new JMenuItem("RECEPTION");
	HotelSystem.add(Recep);
		
	JMenu Adminis = new JMenu("ADMINISTRATION");
        Adminis.setForeground(Color.BLUE);
	menuBar.add(Adminis);
        
        JMenuItem Employe = new JMenuItem("ADD EMPLOYEE");
	Adminis.add(Employe);
        
        Employe.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                try{
                    new AddEmployee().setVisible(true);
                }catch(Exception e ){}
            }
	});
        

        JMenuItem Adroom = new JMenuItem("ADD ROOMS");
	Adminis.add(Adroom);
        
        Adroom.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                try{
                    new AddRooms().setVisible(true);
                }catch(Exception e ){}
            }
	});
        

	Recep.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                new Reception();
            }
	});
        
     
        
        JMenu Logout = new JMenu("EXIT");
        Logout.setForeground(Color.BLUE);
	menuBar.add(Logout);
        
        JMenuItem Signout = new JMenuItem("LOG OUT");
	Logout.add(Signout);
        
       Signout.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                setVisible(false);
                new Login();
            }
	});
        
		
        setSize(1200, 600);
        setLocation(150,100);
	setVisible(true);
        getContentPane().setBackground(Color.WHITE);
    }
}