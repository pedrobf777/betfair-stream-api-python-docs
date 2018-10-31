# OrderChangeMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation type | [optional] 
**id** | **int** | Client generated unique id to link request with response (like json rpc) | [optional] 
**ct** | **str** | Change Type - set to indicate the type of change - if null this is a delta) | [optional] 
**clk** | **str** | Token value (non-null) should be stored and passed in a MarketSubscriptionMessage to resume subscription (in case of disconnect) | [optional] 
**heartbeat_ms** | **int** | Heartbeat Milliseconds - the heartbeat rate (may differ from requested: bounds are 500 to 30000) | [optional] 
**pt** | **int** | Publish Time (in millis since epoch) that the changes were generated | [optional] 
**oc** | [**list[OrderMarketChange]**](OrderMarketChange.md) | OrderMarketChanges - the modifications to account&#39;s orders (will be null on a heartbeat | [optional] 
**initial_clk** | **str** | Token value (non-null) should be stored and passed in a MarketSubscriptionMessage to resume subscription (in case of disconnect) | [optional] 
**conflate_ms** | **int** | Conflate Milliseconds - the conflation rate (may differ from that requested if subscription is delayed) | [optional] 
**segment_type** | **str** | Segment Type - if the change is split into multiple segments, this denotes the beginning and end of a change, and segments in between. Will be null if data is not segmented | [optional] 
**status** | **int** | Stream status: set to null if the exchange stream data is up to date and 503 if the downstream services are experiencing latencies | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


