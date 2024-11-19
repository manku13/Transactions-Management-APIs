# Transaction Management API

Welcome to the Transaction Management API project! This Django-based application is designed to manage financial transactions efficiently. The system supports creating transactions, viewing transaction history, and updating transaction statuses.

## Features

- **Create Transactions**: Easily create new transactions with specified amounts and types.
- **View Transaction History**: Retrieve a list of all transactions for a specific user.
- **Update Transaction Status**: Update the status of existing transactions to reflect their current state.
- **Detailed Transaction View**: Get detailed information about individual transactions.

## Models

### Transaction Model

The `Transaction` model represents a financial transaction with the following fields:

- **amount**: DecimalField storing the monetary value.
- **transaction_type**: CharField indicating DEPOSIT or WITHDRAWAL.
- **user**: ForeignKey linking to the User model.
- **timestamp**: DateTimeField storing the transaction date and time.
- **status**: CharField with values PENDING, COMPLETED, or FAILED.

## API Endpoints

### Create a New Transaction

**POST /api/transactions/**

Create a new transaction.

**Request Body:**
```json
{
    "amount": 100.00,
    "transaction_type": "DEPOSIT",
    "user": 1
}
```

**Response:**
```json
{
    "transaction_id": 1,
    "amount": 100.00,
    "transaction_type": "DEPOSIT",
    "status": "PENDING",
    "user": 1,
    "timestamp": "2024-11-16T10:30:00Z"
}
```

### Retrieve All Transactions for a User

**GET /api/transactions/**

Retrieve all transactions for a specific user.

**Query Parameter:**
- `user_id`: The ID of the user.

**Response:**
```json
{
    "transactions": [
        {
            "transaction_id": 1,
            "amount": 100.00,
            "transaction_type": "DEPOSIT",
            "status": "PENDING",
            "timestamp": "2024-11-16T10:30:00Z"
        },
        {
            "transaction_id": 2,
            "amount": 50.00,
            "transaction_type": "WITHDRAWAL",
            "status": "COMPLETED",
            "timestamp": "2024-11-15T15:00:00Z"
        }
    ]
}
```

### Update Transaction Status

**PUT /api/transactions/{transaction_id}/**

Update the status of an existing transaction.

**Request Body:**
```json
{
    "status": "COMPLETED"
}
```

**Response:**
```json
{
    "transaction_id": 1,
    "amount": 100.00,
    "transaction_type": "DEPOSIT",
    "status": "COMPLETED",
    "timestamp": "2024-11-16T10:30:00Z"
}
```

### Retrieve Transaction Details

**GET /api/transactions/{transaction_id}/**

Retrieve the details of a specific transaction.

**Response:**
```json
{
    "transaction_id": 1,
    "amount": 100.00,
    "transaction_type": "DEPOSIT",
    "status": "COMPLETED",
    "timestamp": "2024-11-16T10:30:00Z"
}
```

## Getting Started

To get started with the Transaction Management API, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the Django development server.
4. Access the API endpoints as described above.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

Happy coding!