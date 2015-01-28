# Questions
## Call API
You're given a function `call_api` that makes takes a 6-character alphanumeric string id and returns a photo associated with that ID. This function is not very "smart": if you're off by even one character case, it will fail. Write a smarter version of this function that will ignore a case mistake in one character.

Input: ge5E9i

Expected: gE5E9i

Make function return picture.

Follow-on: Make this function completely case-insensitive.

## Stock Market
Given an array of integers that are stock prices, find the points at which you would buy and sell.
```
Input: [20, 10, 30, 40, -10]
Output:
	Profit=30
	Buy at 10
	Sell at 40
```

## Implement Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination. If this works properly, when you feed it the string:
```
1c0111001f010100061a024b53535009181c
```
and XOR this against
```
686974207468652062756c6c277320657965
```
Then you should get:
```
746865206b696420646f6e277420706c6179
```