// contracts/MyToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract AndresCoin is ERC20 {
    // wei
    constructor(uint256 initialSupply) ERC20("AndresCoin", "AC") {
        _mint(msg.sender, initialSupply);
    }
}
