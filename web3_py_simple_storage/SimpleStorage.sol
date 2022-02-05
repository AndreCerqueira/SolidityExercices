// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0; // latest - preferences / solidity

contract SimpleStorage {

    uint256 public favoriteNumber = 5;
    
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
  
    mapping(string => uint256) public nameTofavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // view, pure
    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameTofavoriteNumber[_name] = _favoriteNumber;
    }

}