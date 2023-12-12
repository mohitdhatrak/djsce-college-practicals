class TicketReservation extends Thread {
    int vacant = 2, required;

    TicketReservation(int r) {
        required = r;
    }

    public synchronized void run() {
        System.out.println(Thread.currentThread().getName() + ", welcome to ABC Bus service");
        System.out.println("No. of seats left: " + vacant);
        if (required <= vacant) {
            System.out.println(Thread.currentThread().getName() + " - " + required +
                    " tickets have been booked");
            try {
                Thread.sleep(100);
            } catch (Exception e) {
            }
            vacant -= required;
        } else {
            System.out.println("All tickets booked!");
        }
    }
}

class Synchronized {
    public static void main(String args[]) {
        TicketReservation br = new TicketReservation(2);
        Thread t1 = new Thread(br);
        Thread t2 = new Thread(br);
        t1.setName("User1");
        t2.setName("User2");
        t1.start();
        t2.start();
    }
}