import * as readlineSync from 'readline-sync';
class BankAccount {
    AccountNo: number;
    AccountHolderName: string;
    Balance: number;
    constructor(accNo: number, name: string, balance: number) {
        this.AccountNo = accNo;
        this.AccountHolderName = name;
        this.Balance = balance; }
    balanceCheck(): void {
        this.Balance < 0
            ? console.log('Insufficient Balance! Please Deposit.')
            : console.log(`The Balance for ${this.AccountHolderName} is: ${this.Balance}`);  }
    deposit(amount: number): void {
        if (amount > 0) {
            this.Balance += amount;
            console.log(`Amount of ${amount} Deposited Successfully.`);
            this.balanceCheck();
        } else {
            console.log('Invalid deposit amount.');    }  }
    withdraw(amount: number): void {
        if (amount > 0) {
            amount > this.Balance
                ? console.log('Not Enough Balance.')
                : (this.Balance -= amount, console.log(`Amount of ${amount} withdrawn Successfully.`));
            this.balanceCheck();
        } else {
            console.log('Invalid withdrawal amount.');   } }
    calculateInterest(rate: number): void {
        const interest = (this.Balance * rate) / 100;
        this.Balance += interest;
        console.log(`Interest of ${interest.toFixed(2)} added to your account. New balance is: ${this.Balance.toFixed(2)}`);
    }
}
function performTransaction(account: BankAccount): void {
    let action = '';
    do {
        console.log(`\nSelect operation for Account ${account.AccountNo} (${account.AccountHolderName}):`);
        console.log('1. Balance Check');
        console.log('2. Deposit');
        console.log('3. Withdraw');
        console.log('4. Calculate Interest');
        console.log('5. Exit');
        action = readlineSync.question('Enter action number (1-5): ');
        switch (action) {
            case '1':
                account.balanceCheck();
                break;
            case '2':
                const depositAmount = parseFloat(readlineSync.question('Enter amount to deposit: '));
                account.deposit(depositAmount);
                break;
            case '3':
                const withdrawAmount = parseFloat(readlineSync.question('Enter amount to withdraw: '));
                account.withdraw(withdrawAmount);
                break;
            case '4':
                const interestRate = parseFloat(readlineSync.question('Enter the interest rate (in %): '));
                account.calculateInterest(interestRate);
                break;
            case '5':
                console.log('Exiting...');
                break;
            default:
                console.log('Invalid option. Please choose between 1 and 5.');
        }
    } while (action !== '5'); }
function createAccount(): BankAccount {
    const accNo = parseInt(readlineSync.question('Enter account number: '));
    const name = readlineSync.question('Enter account holder name: ');
    const balance = parseFloat(readlineSync.question('Enter initial balance: '));
    return new BankAccount(accNo, name, balance);
}
function selectAccount(users: BankAccount[]): BankAccount {
    console.log('\nSelect the account to perform operations on:');
    users.forEach((user, index) => {
        console.log(`${index + 1}. Account ${user.AccountNo} - ${user.AccountHolderName}`);
    });
    const accountChoice = parseInt(readlineSync.question('Enter the account number (1 to select): '));
    return users[accountChoice - 1] ? users[accountChoice - 1] : users[0];
}
function main() {
    const numUsers = parseInt(readlineSync.question('Enter the number of users: '));
    const users: BankAccount[] = [];
    for (let i = 0; i < numUsers; i++) {
        console.log(`\nCreating account for user ${i + 1}:`);
        const user = createAccount();
        users.push(user);
    }
    let action = '';
    do {
        const selectedAccount = selectAccount(users);
        performTransaction(selectedAccount);
        action = readlineSync.question('Do you want to select another account? (y/n): ').toLowerCase();
    } while (action === 'y');
    console.log('Exiting program...');
}
main();
