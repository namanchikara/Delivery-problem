# Vehicle Routing Problem with capacity and time boundations, i.e Max Count of orders(capacity) a truck can handle and Max Time alloted to a truck until which it has to reach a society and deliver goods there.

We have latitude and longitude points of N societies, order count of these societies, I also have latitude and longitude points of a warehouse from where the trucks will deploy and will be sent to these various societies(like Amazon deliveries). A truck can deliver maximum 350 orders (order count < 350). Now we determine a pattern in which the trucks should be deployed in such a way that a minimum number of trips occur.

There are no restrictions on the number of trucks.

Solved it in python using heuristic algorithm ( https://en.wikipedia.org/wiki/Travelling_salesman_problem ) 
