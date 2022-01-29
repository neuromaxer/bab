pragma solidity ^0.6.0;

contract SimpleBank {
    mapping(address => uint256) private balances;
    address public owner;
    event LogDepositMade(address accountAddress, uint256 amount);

    constructor() public {
        owner = msg.sender;
    }

    function deposit() public payable returns (uint256) {
        require((balances[msg.sender] + msg.value) >= balances[msg.sender], _);

        balances[msg.sender] += msg.value;

        emit LogDepositMade(msg.sender, msg.value); // fire event

        return balances[msg.sender];
    }

    function withdraw(uint256 withdrawAmount) public returns (uint256 remainingBal) {
        require(withdrawAmount <= balances[msg.sender], "Insufficient funds.");

        balances[msg.sender] -= withdrawAmount;

        msg.sender.transfer(withdrawAmount);

        return balances[msg.sender];
    }

    function balance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
