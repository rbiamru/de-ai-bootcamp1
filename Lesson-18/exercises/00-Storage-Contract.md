# Exercise 1: Understanding Blockchain Storage

In this exercise, you will create a simple storage smart contract to understand how data is stored on the blockchain and how to interact with storage variables.

## Steps

1. Set up the project:

   ```bash
   mkdir storage-demo
   cd storage-demo
   npm init -y
   npm install hardhat
   npx hardhat init
   ```

2. Create the storage contract (contracts/Storage.sol):

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.20;

   contract Storage {
       // Fixed storage slots
       string public text;                    // slot 0
       uint256 public number;                 // slot 1
       bool public flag;                      // slot 2
       address public owner;                  // slot 3
       
       // Dynamic storage
       mapping(address => uint256) public balances;    // slot 4
       string[] public messages;                       // slot 5 (length), data at keccak256(5)

       // Events for tracking changes
       event TextChanged(string oldText, string newText);
       event NumberChanged(uint256 oldNumber, uint256 newNumber);
       
       constructor() {
           owner = msg.sender;
       }
       
       // Store text - demonstrates basic storage
       function setText(string memory newText) public {
           string memory oldText = text;
           text = newText;
           emit TextChanged(oldText, newText);
       }
       
       // Store number - demonstrates value types
       function setNumber(uint256 newNumber) public {
           uint256 oldNumber = number;
           number = newNumber;
           emit NumberChanged(oldNumber, newNumber);
       }
       
       // Demonstrate mapping storage
       function setBalance(address account, uint256 amount) public {
           balances[account] = amount;
       }
       
       // Demonstrate dynamic array storage
       function addMessage(string memory message) public {
           messages.push(message);
       }
       
       // View storage slots directly
       function getStorageSlot(uint256 slot) public view returns (bytes32) {
           bytes32 value;
           assembly {
               value := sload(slot)
           }
           return value;
       }
       
       // Get mapping storage location
       function getBalanceLocation(address account) public pure returns (bytes32) {
           return keccak256(abi.encode(account, 4)); // slot 4 is balances mapping
       }
       
       // Get dynamic array element location
       function getMessageLocation(uint256 index) public pure returns (bytes32) {
           bytes32 slot = keccak256(abi.encode(5)); // slot 5 is messages array
           return bytes32(uint256(slot) + index);
       }
   }
   ```

3. Create deployment script (scripts/deploy.ts):

   ```typescript
   import { ethers } from "hardhat";

   async function main() {
     const Storage = await ethers.getContractFactory("Storage");
     const storage = await Storage.deploy();
     await storage.deployed();

     console.log("Storage deployed to:", storage.address);

     // Demonstrate storage operations
     await storage.setText("Hello, Storage!");
     await storage.setNumber(42);
     await storage.setBalance(storage.address, 100);
     await storage.addMessage("First Message");

     // Read storage slots
     const slot0 = await storage.getStorageSlot(0);
     const slot1 = await storage.getStorageSlot(1);
     console.log("Slot 0 (text):", slot0);
     console.log("Slot 1 (number):", slot1);

     // Get mapping storage location
     const balanceLocation = await storage.getBalanceLocation(storage.address);
     const balanceSlot = await storage.getStorageSlot(balanceLocation);
     console.log("Balance storage location:", balanceLocation);
     console.log("Balance value:", balanceSlot);
   }

   main()
     .then(() => process.exit(0))
     .catch((error: Error) => {
       console.error(error);
       process.exit(1);
     });
   ```

4. Create test file (test/Storage.ts):

   ```typescript
   import { expect } from "chai";
   import { ethers } from "hardhat";
   import { Contract } from "ethers";
   import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/signers";

   describe("Storage", function () {
     let storage: Contract;
     let owner: SignerWithAddress;

     beforeEach(async function () {
       [owner] = await ethers.getSigners();
       const Storage = await ethers.getContractFactory("Storage");
       storage = await Storage.deploy();
       await storage.deployed();
     });

     it("Should store and retrieve text", async function () {
       await storage.setText("Hello");
       expect(await storage.text()).to.equal("Hello");
     });

     it("Should store and retrieve number", async function () {
       await storage.setNumber(42);
       expect(await storage.number()).to.equal(42);
     });

     it("Should store and retrieve balances", async function () {
       const address = storage.address;
       await storage.setBalance(address, 100);
       expect(await storage.balances(address)).to.equal(100);
     });
   });
   ```

## Expected Output

- Deployed storage contract
- Successfully stored and retrieved values
- Correct storage slot values
- Understanding of storage layout
