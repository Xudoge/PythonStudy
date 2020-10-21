USTRUCT(BlueprintType)
struct Ftest02_Struct : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()
 
 
	UPROPERTY()
	int32	id;
 
	UPROPERTY()
	FString	Name;
 
	UPROPERTY()
	float	value;
 
};
