import random
import time

class Package:
    """
    Represents a package sent from sender to receiver.

    Attributes:
        id (int): Unique identifier of the package.
        time (float): Estimated time for transmitting the package.
    """
    def __init__(self, id, package_time=0.0):
        self.id = id
        self.time = package_time

class Sender:
    """
    Simulates the package sender.

    Attributes:
        number_of_packages (int): Total number of packages to be sent.
        window_size (int): Transmission window size (Selective Repeat).
        time_to_wait (float): Maximum time before retransmission.
        packages (list): List of Package objects.
    """
    def __init__(self, number_of_packages, window_size):
        self.number_of_packages = number_of_packages
        self.window_size = window_size
        self.time_to_wait = 4.0
        self.packages = []

    def send_all_packages(self):
        """
        Generates and sends all packages with random transmission times.
        """
        for i in range(1, self.number_of_packages + 1):
            time_value = random.uniform(0.1, 5.0)
            self.packages.append(Package(i, time_value))

    def display(self):
        """
        Displays the IDs of the sent packages.
        """
        print("sender:", ' '.join(str(pkg.id) for pkg in self.packages))

class Receiver:
    """
    Simulates the package receiver.

    Attributes:
        received_packages (list): List of successfully received packages.
    """
    def __init__(self):
        self.received_packages = []

    def receive(self, package):
        """
        Adds a received package to the receiver's buffer.

        Args:
            package (Package): The received package.
        """
        self.received_packages.append(package)

    def display(self):
        """
        Displays the IDs of the received packages.
        """
        print("receiver:", ' '.join(str(pkg.id) for pkg in self.received_packages))

def selective_repeat(sender, receiver):
    """
    Selective Repeat algorithm for reliable packet transmission.
    Simulates packet loss, ACK loss, and retransmissions.

    Args:
        sender (Sender): The sender object containing the packages.
        receiver (Receiver): The receiver object that receives the packages.
    """
    acked = set()
    window_start = 1
    sended = [False] * (sender.number_of_packages + 1)

    print("Time for packages:")
    for pkg in sender.packages:
        print(pkg.id, f"{pkg.time:.2f}")

    while window_start <= sender.number_of_packages:
        window_end = min(window_start + sender.window_size - 1, sender.number_of_packages)

        sender.display()
        receiver.display()
        print(f"Current window: [{ ' '.join(str(i) for i in range(window_start, window_end + 1)) }]")

        for i in range(window_start, window_end + 1):
            if not sended[i]:
                pkg = sender.packages[i - 1]
                if random.random() < 0.2:
                    print(f"Package {pkg.id} lost during transmission to receiver!")
                    continue
                print(f"Sending package {pkg.id}... (time: {pkg.time:.2f})")
                sended[i] = True

        unacked = [(pkg.id, pkg.time) for pkg in sender.packages[window_start - 1:window_end] if pkg.id not in acked]
        if not unacked:
            window_start = window_end + 1
            continue

        unacked.sort(key=lambda x: x[1])

        for pkg_id, pkg_time in unacked:
            if pkg_time < sender.time_to_wait and sended[pkg_id]:
                if random.random() < 0.15:
                    print(f"ACK for package {pkg_id} lost!")
                    continue
                print(f"Received ACK for package {pkg_id}")
                acked.add(pkg_id)
                receiver.receive(sender.packages[pkg_id - 1])
                while window_start in acked:
                    window_start += 1
            else:
                if sended[pkg_id]:
                    print(f"Timeout for package {pkg_id}")
                new_time = random.uniform(0.1, 4.0)
                sender.packages[pkg_id - 1].time = new_time
                sended[pkg_id] = False
                print(f"Will resend package {pkg_id} with new time: {new_time:.2f}")
            break

        print()
        time.sleep(1)

    print("\nAll packages successfully transmitted!")

def main():
    """
    Main function that runs the Selective Repeat protocol simulation.
    Initializes the sender, receiver, and starts the transmission process.
    """
    num = int(input("Enter the number of packages: "))
    print("Packages:", ' '.join(str(i) for i in range(1, num + 1)))
    win_size = random.randint(2, min(5, num // 2))
    print(f"\nWindow size: {win_size}")

    sender = Sender(num, win_size)
    sender.send_all_packages()
    receiver = Receiver()

    selective_repeat(sender, receiver)

    print("\nReceiver's buffer (order of received packages):", ' '.join(str(pkg.id) for pkg in receiver.received_packages))
    print("\nSender's buffer (order of sent packages):", ' '.join(str(pkg.id) for pkg in sender.packages))

if __name__ == "__main__":
    main()
