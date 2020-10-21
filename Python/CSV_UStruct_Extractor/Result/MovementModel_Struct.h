USTRUCT(BlueprintType)
struct FMovementModel_Struct : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()
 
 
	UPROPERTY()
	TArray<FString>	VelocityDirection;
 
	UPROPERTY()
	TArray<FString>	LookingDirection;
 
	UPROPERTY()
	TArray<FString>	Aiming;
 
};
