// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Bank {
    mapping(address => uint256) public balanceOf;

    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);

    function deposit() external payable {
        require(msg.value > 0, "deposit must be positive");
        balanceOf[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external {
        require(amount > 0, "withdrawal must be positive");
        require(amount <= balanceOf[msg.sender], "insufficient deposited balance");
        balanceOf[msg.sender] -= amount; // Effects before interaction prevents re-entrancy.
        (bool sent, ) = payable(msg.sender).call{value: amount}("");
        require(sent, "transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    function showBalance() external view returns (uint256) {
        return balanceOf[msg.sender];
    }
}
