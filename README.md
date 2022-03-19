# Project_3_TiX
Final project. TiX marketplace

# Capstone Project -  NFT Ticketing Platform
​
## Executive Summary
​
Create a decentralized ticketing & digital merchandise platform to empower artists and creators to engage directly with fans through events and exclusive content. This platform would leverage blockchain technology,  lower fees, and customer loyalty to become the premier ticketing platform in the marketplace.
​
## Value Proposition:
​
Lower fees than traditional ticketing platforms
Secure transactions verified on the blockchain 
Royalty payments from merchandise + ticketing revenue for event organizer
Robust secondary market for tickets and merchandise driving royalty payments
Aggregate data from all events on our platform to provide an analytics platform for event organizers 
​
​
## Project Goals:
​
  ### Core Goals:
​
  - Create Token to be used on platform as currency - “TIX”
  - Create contract in solidity 
  - Create functionality for NFT ticket at point of access
  - QR code to access event
  - Create smart contract to mint “event” tickets
    - Limit supply to event capacity
  - Create smart contract for event attendees to purchase tickets from directly from event creator
    - Royalties to event organizer (artist)
    - Royalties to platform
  - Create smart contract for event attendees to purchase tickets on secondary market (non-owner)
    - Royalties to event organizer (artist)
    - Royalties to platform
  - Use streamlit / javascript to create front end interface
​
​
  ### Supplemental Goals:
​
  - Create front end interface for secondary sales platform
  - Run analytics for revenue projections 
    - Initial ticket mint supply
    - Secondary ticket sales
    - Incentive sales
  - Create smart contract for users to trade NFT merchandise from these events
    - Royalties to event organizer (artist)
    - Royalties to platform 
  - Incentivize users to engage platform
    - Concerts - airdrop clip / song recordings to event attendees
    - Sports - airdrop clip of biggest in game moment
    - Photography/ Recordings from event 
    - Loyalty rewards for holders of native token - Tokenomics
    - Exclusive events 
    - Loyalty rewards for largest collectors of individual artists / teams 
    - Exclusive NFTs
​
​
## Back-end Development:
​
​
### Tech Used
​
Solidity- v 0.6.0
Metamask
Ganache
Python
Streamlit / Javascript 
QR code generator
Web app for creating ticket visual
Remix
​
​
## Frontend Development:
​
### Tech Used
​
Streamlit
QR Code Generator
Python
​
​
## Project Deployment:
​
​
### Smart Contract Compliling & Deployment
​
The screenshots below are showing the smart contract compilation, deployment, and connection to the Metamask wallets interacting with the contract.
​
![smart contract compiling](https://user-images.githubusercontent.com/91380617/159125772-2c032f05-2478-4837-bbf6-27210e8deba8.png)
​
![smart contract deployment confirmation](https://user-images.githubusercontent.com/91380617/159125783-bcd5801a-c412-408b-b5cb-41511228c99c.png)
​
![wallet 1](https://user-images.githubusercontent.com/91380617/159125778-c5be1739-32ce-4248-a4fb-d971d242f1b7.png)
​
![wallet 2](https://user-images.githubusercontent.com/91380617/159125781-1659ff28-86e6-4b1a-ba02-1abbea2fa3e7.png)
​
​
### Visualizing Ticket Prototype
​
Here we mocked what a potential NFT ticket would look like. You'll notice that we added a QR code to the ticket to allow for event access. 
​
![bm_ticket](https://user-images.githubusercontent.com/91380617/159125714-09b58baa-6545-44db-8855-72e49f51f865.png)
​
​
### NFT Marketplace 
​
This is an early look at what a potential front end interface would look like for customers.
​
![selecting ticket](https://user-images.githubusercontent.com/91380617/159125767-f1e89b7b-bac3-4f5b-842b-97fc706ab0de.png)
​
​
### Transaction Confirmation 
​
Here is confirmation that the tickets were purchased.
​
![transaction confirmation](https://user-images.githubusercontent.com/91380617/159125757-e195a9ab-cc5b-421a-8c44-22f284c8ce06.png)
​
​
## Feasibility Analysis:
​
The following assumptions were made when conducting this analysis:
​
Ticketmaster / Stubhub typically add a surcharge of at least 10% on each sale
See citations for this figure 
Estimated cost for running the platform and deploying the smart contracts / initial ticket mint is $250,000
See citations for this 
​
Based on our assumptions above, here is a rough estimate for the platform’s Net Income for a single large scale (20,000+ event attendees) event. These calculations do not factor in merchandise sales / secondary sales as we do not have these operations functioning yet. With our estimated operating costs our platform would break even after 3 large scale events.
​
![feasibility_analysis](https://user-images.githubusercontent.com/91380617/159125755-ea04085b-49b9-4215-97c6-fdc210d14984.png)
​
​
## Additional Development - Project Roadmap:
​
These are the next features we would focus on building to enhance our platform and continue to add value to the ticket buying experience. 
​
1. Create front end interface for secondary sales platform
2. Run analytics for revenue projections 
3. Secondary ticket sales
4. Incentive sales
5. Create smart contract for users to trade NFT merchandise from these events
6. Incentivize users to engage platform
7. Launch native token for platform
​
### User Benefits:
​
These next set of features would empower the user base through a functioning secondary market (peer to peer sales) and adding loyalty rewards to the user base. These benefits would encourage users to remain engaged on the platform and be a key selling point for new customer acquisition. 
​
### Event Organizer Benefits:
​
There are also benefits towards event sponsors / organizers via royalties on secondary NFT sales and NFT merchandise sales. In addition to increasing the revenue for each event through royalties from ticket / merchandising sales we would aggregate the platform’s data to provide an analytics platform for event organizers to project revenues, streamline efficiencies, and provide benchmark metrics to similar events. 
​
This would likely be deployed through a second front end interface that the event sponsor / organizer would log in to with the wallet they used to deploy the initial smart contract to mint the ticket supply.
​
 
## Conclusion:
​
We originally had written much more complex code with a number of the functions we outlined in our future project roadmap. However, we found that linking the complex code with Streamlit was a challenge. 
​
This led us to making the executive decision to simplify the smart contract and limit the amount of functions within the smart contract to have a working proof of concept for project completion. 
​
Even with limited functionality we believe our platform has the ability to streamline the current ticketing exchange ecosystem and provide a platform that excites users / organizers to utilize our blockchain platform. 
​
## Citations:
​
​
https://www.youtube.com/watch?v=0i6V2hOosB4
​
https://dev.to/dabit3/building-scalable-full-stack-apps-on-ethereum-with-polygon-2cfb
​
https://github.com/Andreasaarrestad/ethereumTicketSystem
​
https://appinventiv.com/blog/cost-of-nft-marketplace-development/
