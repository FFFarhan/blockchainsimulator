Blockchain Simulator
====================

A simple blockchain simulator built using Python and Flask. This project mimics a decentralized ledger where blocks can be mined, transactions are recorded, and users can explore the blockchain through a web interface.

Features
--------

-   **Blockchain Visualization**: View the entire blockchain as a series of blocks.
-   **Mining Simulator**: Mine new blocks by finding proof of work and add them to the blockchain.
-   **Interactive Web Interface**: A clean and intuitive Flask web app to interact with the blockchain.
-   **Proof of Work**: Simulates the mining process by solving a computational puzzle to add new blocks to the chain.

Project Structure
-----------------


```bash
/blockchain-simulator
├── app.py                  # Main Flask application
├── /templates              # HTML templates for rendering web pages
│   ├── index.html          # Home page
│   ├── mine_result.html    # Mining result page
│   └── blocks.html         # Blockchain visualization page
├── /static                 # Static files (CSS, JS, images)
│   └── styles.css          # Styling for the web app
└── requirements.txt        # Python dependencies
```

Technologies Used
-----------------

-   **Python**: The primary programming language.
-   **Flask**: A micro web framework to build the web app.
-   **HTML/CSS**: Used for the front-end design and layout.
-   **Hashlib**: For cryptographic hash functions, ensuring the immutability of blocks in the blockchain.

Installation
------------

Follow these steps to run the project locally.

### 1\. Clone the repository



`git clone https://github.com/FFFarhan/blockchainsimulator.git`
`cd blockchainsimulator`

### 2\. Install dependencies

Make sure you have `pip` installed, then install the required Python libraries:



`pip install -r requirements.txt`

### 3\. Run the application

To start the Flask server, use:


`python app.py`

By default, the app will be accessible at `http://127.0.0.1:5000/`.

Endpoints
---------

-   `/` (GET): **Home Page** - Introduction to blockchain and navigation options.
-   `/mine` (GET): **Mine a Block** - Simulates mining and adds a new block to the blockchain.
-   `/blocks` (GET): **View Blockchain** - Displays all the blocks in the current blockchain.

How It Works
------------

### Blockchain Structure

The blockchain is a sequence of blocks where each block contains:

-   `index`: The position of the block in the chain.
-   `timestamp`: The date and time when the block was created.
-   `data`: Information stored in the block (transactions or messages).
-   `previous_hash`: The hash of the previous block, ensuring the integrity of the chain.
-   `hash`: The unique hash of the current block, calculated using SHA-256.

### Proof of Work (PoW)

To mine a new block, the app uses a proof of work algorithm. This computational puzzle requires miners to find a number that satisfies a specific condition. Once the proof of work is found, a new block is added to the blockchain, and a small reward (a transaction) is issued to the miner.

### Web Interface

The Flask app allows users to interact with the blockchain via a web interface:

-   **Home Page**: An introduction to the blockchain concept and a guide to interact with the app.
-   **Blockchain View**: Displays the list of blocks in a table format, showing details such as index, timestamp, and hash.
-   **Mining Result**: After mining a new block, a page shows the new block details.


Contributing
------------

Feel free to fork the repository and submit pull requests for new features or improvements. If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature-branch`).
3.  Make your changes.
4.  Commit your changes (`git commit -am 'Add new feature'`).
5.  Push to the branch (`git push origin feature-branch`).
6.  Submit a pull request.
