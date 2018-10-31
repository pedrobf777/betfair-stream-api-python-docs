# MarketDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**venue** | **str** |  | [optional] 
**race_type** | **str** |  | [optional] 
**settled_time** | **datetime** |  | [optional] 
**timezone** | **str** |  | [optional] 
**each_way_divisor** | **float** |  | [optional] 
**regulators** | **list[str]** | The market regulators. | [optional] 
**market_type** | **str** |  | [optional] 
**market_base_rate** | **float** |  | [optional] 
**number_of_winners** | **int** |  | [optional] 
**country_code** | **str** |  | [optional] 
**line_max_unit** | **float** | For Handicap and Line markets, the maximum value for the outcome, in market units for this market (eg 100 runs). | [optional] 
**in_play** | **bool** |  | [optional] 
**bet_delay** | **int** |  | [optional] 
**bsp_market** | **bool** |  | [optional] 
**betting_type** | **str** |  | [optional] 
**number_of_active_runners** | **int** |  | [optional] 
**line_min_unit** | **float** | For Handicap and Line markets, the minimum value for the outcome, in market units for this market (eg 0 runs). | [optional] 
**event_id** | **str** |  | [optional] 
**cross_matching** | **bool** |  | [optional] 
**runners_voidable** | **bool** |  | [optional] 
**turn_in_play_enabled** | **bool** |  | [optional] 
**price_ladder_definition** | [**PriceLadderDefinition**](PriceLadderDefinition.md) | Definition of the price ladder type and any related data. | [optional] 
**key_line_definition** | [**KeyLineDefinition**](KeyLineDefinition.md) | Definition of a markets key line selection (for valid markets), comprising the selectionId and handicap of the team it is applied to. | [optional] 
**suspend_time** | **datetime** |  | [optional] 
**discount_allowed** | **bool** |  | [optional] 
**persistence_enabled** | **bool** |  | [optional] 
**runners** | [**list[RunnerDefinition]**](RunnerDefinition.md) |  | [optional] 
**version** | **int** |  | [optional] 
**event_type_id** | **str** | The Event Type the market is contained within. | [optional] 
**complete** | **bool** |  | [optional] 
**open_date** | **datetime** |  | [optional] 
**market_time** | **datetime** |  | [optional] 
**bsp_reconciled** | **bool** |  | [optional] 
**line_interval** | **float** | For Handicap and Line markets, the lines available on this market will be between the range of lineMinUnit and lineMaxUnit, in increments of the lineInterval value. e.g. If unit is runs, lineMinUnit&#x3D;10, lineMaxUnit&#x3D;20 and lineInterval&#x3D;0.5, then valid lines include 10, 10.5, 11, 11.5 up to 20 runs. | [optional] 
**status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


