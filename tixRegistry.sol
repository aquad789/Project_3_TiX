pragma solidity ^0.5.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
contract TIXRegistry is ERC721Full {
    constructor() public ERC721Full("TIXToken", "TIX") {}
    struct TIXNFT {
        string name;
        string artist;
        uint256 appraisalValue;
    }
    mapping(uint256 => TIXNFT) public TIXCollection;
    event Appraisal(uint256 tokenId, uint256 TIXValue, string reportURI);
    function buy_TIXNFT(
        address owner,
        // string memory name,
        // string memory artist,
        // uint256 initialTIXValue,
        string memory tokenURI
    ) public payable returns (uint256) {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);
        // TIXCollection[tokenId] = TIXNFT(name, artist, initialTIXValue);
        return tokenId;
    }
    // function newTIXVALUE(
      //  uint256 tokenId,
       // uint256 newTIXValue,
       //  string memory reportURI
    //public returns (uint256) {
       // TIXCollection[tokenId].appraisalValue = newTIXValue;
        //emit Appraisal(tokenId, newTIXValue, reportURI);
        //return TIXCollection[tokenId].appraisalValue;
    //}
}