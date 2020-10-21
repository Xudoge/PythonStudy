USTRUCT(BlueprintType)
struct Ftest_Struct : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()
 
 
	UPROPERTY()
	int32	id;
 
	UPROPERTY()
	TArray<FString>	Name;
 
	UPROPERTY()
	float	value;
 
};
