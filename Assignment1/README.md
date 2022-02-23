# Assignment 2 
### 18103033 Shayan Yaseen

## Use-Case Diagram Using PlantUML

### Code
```
@startuml Donna_FinancialAssistant

actor "User" as user
actor "Amazon\nPrize\nTracker" as APT
actor "Chat Bot" as chat

left to right direction
skinparam packageStyle rectangle


rectangle Donna_FinancialAssistant{

(Income Details) as income
(Expenditure Details) as expenditure
(List Requirements) as list
(Alternatve Savings) as alternative
(Add Items to Wishlist) as addToWishlist
(Wishlist Price History) as WishlistPriceHistory
(Price History) as priceHistory
(Price Drop Probability) as dropProbabilty
(Login) as login

}

income ..> login : include
expenditure  ..> login : include
list ..> login : include
alternative ..> login : include
addToWishlist ..> login : include
WishlistPriceHistory ..> login : include

user -- income
user -- expenditure
user -- list
user -- alternative
user -- addToWishlist
user -- WishlistPriceHistory

chat --addToWishlist
chat -- WishlistPriceHistory
chat -- priceHistory
chat --dropProbabilty

APT -- priceHistory
APT -- dropProbabilty

@enduml
```
### Image
<img src="https://github.com/ShayanYaseen/SoftwareTesting/Assignment1/SequenceDiagram.png">

## Sequence Diagram Using PlantUML

### Code
```
@startuml SequenceDiagram
skinparam style strictuml
skinparam backgroundColor #EEEBDC
skinparam sequenceMessageAlign center
title DONNA - Financial Assistant
actor User as A
participant Server as B
participant ChatBot as C
participant "Amazon Tracker" as D
participant "Stock Price Tracker" as E
autonumber

A -> B :Request SignUp Form
activate B#LightGray
B --> A :SignUp Form
deactivate B
A -> B : Fill Details and Submit
activate B#LightGray
group#Gold #LightGreen SignUp [Success]
    B -> A: Authentication Accepted
else #LightPink Failure
    B -> A: Authentication Rejected
end
deactivate B
|||
A -> B :Request Login Form
activate B#LightGray
B --> A :Login Form
deactivate B
A -> B : Fill Details and Submit
activate B#LightGray
group#Gold #LightGreen Login [Success]
    B -> A: Welcome!!
else #LightPink Failure
    B -> A: Invalid Username OR Passsword
end
deactivate B
|||
group#LightGray Details Submission [Request Form] 
    A -> B :Request Details Form
    activate B#LightGray
    B --> A :Details Form
    deactivate B
    A -> B :Fill Details and Submit
    activate B#LightGray
    B -> A :Confirmation
    deactivate B
else Submit via ChatBot
    A -> C :Submit Details
    activate C#LightGray
    C -> B :Send Details
    activate B#LightGray
    B --> C :Confirmation
    deactivate B 
    C --> A :Confirmation
    deactivate C
end
|||
A -> C :Submit Wishlist 
activate C#LightGray
C -> D :Checks Price
activate D#LightGray
D --> C :Price
deactivate D
C --> A :Estimated Price Suggested
deactivate C
|||
A -> C :Request For Stock Price 
activate C#LightGray
C -> E :Request For Stock Price Fetch
activate E #LightGray
D --> C :Stock Price
deactivate E
C --> A :ERequested Stock Price
deactivate C
@enduml

```
### Image
<img src="https://github.com/ShayanYaseen/SoftwareTesting/Assignment1/UseCase.jpeg">

