# OrderFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_overall_position** | **bool** | Returns overall / net position (See: OrderRunnerChange.mb / OrderRunnerChange.ml). Default&#x3D;true | [optional] 
**account_ids** | **list[int]** | Internal use only &amp; should not be set on your filter (your subscription is already locked to your account). If set subscription will fail. | [optional] 
**customer_strategy_refs** | **list[str]** | Restricts to specified customerStrategyRefs; this will filter orders and StrategyMatchChanges accordingly (Note: overall postition is not filtered) | [optional] 
**partition_matched_by_strategy_ref** | **bool** | Returns strategy positions (See: OrderRunnerChange.smc&#x3D;Map&lt;customerStrategyRef, StrategyMatchChange&gt;) - these are sent in delta format as per overall position. Default&#x3D;false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


