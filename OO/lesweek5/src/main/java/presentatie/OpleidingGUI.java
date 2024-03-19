package presentatie;

import javax.swing.*;

public class OpleidingGUI {
    private JPanel mainPanel;
    private JPanel input;
    private JLabel vakNaam1;
    private JLabel vakNaam2;
    private JLabel vakNaam3;
    private JLabel vakNaam4;
    private JLabel vakNaam5;
    private JLabel vakNaam6;
    private JTextField punten1;
    private JTextField punten2;
    private JTextField punten3;
    private JTextField punten5;
    private JTextField punten6;
    private JTextField punten4;
    private JLabel MaxScore;
    private JLabel Resultaat;
    private JTextField textField1;
    private JButton button1;
    private JButton button2;


    public OpleidingGUI() {

        RapportGUI rapport = new RapportGUI();

    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("OpleidingGUI");
        frame.setContentPane(new OpleidingGUI().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500,500);
        frame.setVisible(true);
    }
}
