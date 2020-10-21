USTRUCT(BlueprintType)
struct Ftest01_Struct : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()
 
 
	UPROPERTY()
	int32	id;
 
	UPROPERTY()
	FString	Name;
 
	UPROPERTY()
	float	value;
 
};
