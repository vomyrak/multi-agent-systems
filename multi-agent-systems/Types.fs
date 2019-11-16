﻿module Types

type Activity =
    | Building
    | Hunting
    | Nothing

type Fauna = 
    | Rabbos
    | Staggi

type VotingSystem =
    | InstantRunoff
    | RunOff
    | Approval
    | Boda
    
type Agent = {
    Name : string;
    Selflessness : float; 
    BuildingAptitude : float;
    HuntingAptitude : float;
    PoliticalApathy : float;
    FavouriteFood : Fauna;
    Mood : int;
    Energy : float;
    TodaysActivity : Activity * float;
    Opinions : (string * float) list    // Perhaps change string to int and add an ID field
    }

type AgentActions = {
    EnergyPutIn : float;
    HowVoted : string;  // Change to better type
    Opinions : (string * float) list
    }



