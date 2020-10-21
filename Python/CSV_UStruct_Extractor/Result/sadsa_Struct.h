USTRUCT(BlueprintType)
struct Fsadsa_Struct : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()
 
 
	UPROPERTY()
	bool	boolS;
 
	UPROPERTY()
	TArray<bool>	bool_array;
 
	UPROPERTY()
	FString	text;
 
	UPROPERTY()
	TArray<FVector>	vector;
 
	UPROPERTY()
	FRotator	Rotator;
 
	UPROPERTY()
	FTransform	Transfrom;
 
	UPROPERTY()
	FVector2D	vec2;
 
};
